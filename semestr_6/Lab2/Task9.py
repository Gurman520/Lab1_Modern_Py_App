import argparse


def format_text_block(frame_height, frame_width, file_name):
    height = 0
    with open(file_name) as file:
        while height < frame_height:
            line = ''
            for width in range(frame_width):
                st = file.read(1)
                if st == '\n':
                    print()
                    height += 1
                    st = file.read(1)
                    while st == '\n':
                        print()
                        height += 1
                        st = file.read(1)
                line += st
            height += 1
            print(line)


parser = argparse.ArgumentParser()

parser.add_argument("--frame-height", type=int, default=0, dest="height")

parser.add_argument("--frame-width", type=int, default=0, dest="width")

parser.add_argument("file_name", type=str, default="empty")


args = parser.parse_args()
format_text_block(args.height, args.width, args.file_name)
