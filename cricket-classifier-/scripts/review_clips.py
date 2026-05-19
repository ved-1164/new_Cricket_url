"""
Binary keep/trash reviewer for per-class clip folders.

After segment_clips.py runs, each class folder contains clips that mostly show
the right shot — but some will be junk (title cards, crowd, scoreboards, etc.).
This tool loop-plays each clip and lets you keep or trash it with one key.

Keys:
  k or SPACE   keep the clip (no action)
  x            trash (move to data/clips/_trash/)
  z            undo last move
  n            next (alias for keep)
  Q            quit (capital, so you don't quit by accident)

Usage:
    python scripts/review_clips.py                    # review every class folder
    python scripts/review_clips.py --class drive      # only one class
    python scripts/review_clips.py --class drive --start 20
"""

import argparse
import shutil
import sys
from collections import deque
from pathlib import Path

try:
    import cv2
except ImportError:
    sys.exit("opencv-python not installed. Run: pip install -r requirements.txt")


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLIPS_DIR = PROJECT_ROOT / "data" / "clips"
TRASH = CLIPS_DIR / "_trash"

CLASS_NAMES = ["drive", "cut", "pull_hook", "sweep", "defensive", "glance", "innovative", "other"]

KEEP_KEYS = {ord("k"), ord(" "), ord("n")}
TRASH_KEY = ord("x")
UNDO = ord("z")
QUIT = ord("Q")

LEGEND = ["k/SPACE  keep    x  trash    z  undo    Q  quit"]


def draw_overlay(frame, title: str):
    h, w = frame.shape[:2]
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, 30), (0, 0, 0), -1)
    cv2.putText(overlay, title, (8, 22), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (255, 255, 255), 1, cv2.LINE_AA)
    band_h = 30
    cv2.rectangle(overlay, (0, h - band_h), (w, h), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.65, frame, 0.35, 0, frame)
    cv2.putText(frame, LEGEND[0], (8, h - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (255, 255, 255), 1, cv2.LINE_AA)


def play_until_key(clip: Path, title: str) -> int:
    cap = cv2.VideoCapture(str(clip))
    if not cap.isOpened():
        print(f"  cannot open {clip.name}, skipping")
        return ord("k")
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    delay = max(1, int(1000 / fps))
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            draw_overlay(frame, title)
            cv2.imshow("review_clips", frame)
            k = cv2.waitKey(delay) & 0xFF
            if k == 255:
                continue
            return k
    finally:
        cap.release()


def move_to(src: Path, dst_dir: Path) -> Path:
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    if dst.exists():
        dst = dst_dir / f"{src.stem}_dup{src.suffix}"
    shutil.move(str(src), str(dst))
    return dst


def review_class(cls: str, start: int) -> None:
    class_dir = CLIPS_DIR / cls
    clips = sorted(class_dir.glob("*.mp4"))
    if not clips:
        print(f"  (no clips in {cls})")
        return

    print(f"\n=== {cls}: {len(clips)} clips, starting at {start} ===")
    history: deque = deque(maxlen=20)
    i = start
    while i < len(clips):
        clip = clips[i]
        if not clip.exists():
            i += 1
            continue
        title = f"[{cls}] [{i+1}/{len(clips)}]  {clip.name}"
        k = play_until_key(clip, title)
        if k == QUIT:
            print("Quit.")
            sys.exit(0)
        if k == UNDO:
            if not history:
                print("  nothing to undo")
                continue
            moved_to, prev_i = history.pop()
            if moved_to.exists():
                shutil.move(str(moved_to), str(clips[prev_i]))
                print(f"  UNDO -> restored {clips[prev_i].name}")
            i = prev_i
            continue
        if k == TRASH_KEY:
            moved = move_to(clip, TRASH)
            history.append((moved, i))
            print(f"  [{i+1}] TRASH")
            i += 1
            continue
        if k in KEEP_KEYS:
            print(f"  [{i+1}] keep")
            i += 1
            continue
        print(f"  unknown key, replay")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--class", dest="cls", help="Only this class")
    ap.add_argument("--start", type=int, default=0, help="Resume at this index within the class")
    args = ap.parse_args()

    classes = [args.cls] if args.cls else CLASS_NAMES
    for cls in classes:
        review_class(cls, args.start if args.cls else 0)

    cv2.destroyAllWindows()

    print("\nClass counts after review:")
    for cls in CLASS_NAMES:
        n = len(list((CLIPS_DIR / cls).glob("*.mp4")))
        print(f"  {cls:12s} {n}")
    trash_n = len(list(TRASH.glob("*.mp4"))) if TRASH.exists() else 0
    print(f"  {'_trash':12s} {trash_n}")


if __name__ == "__main__":
    main()
