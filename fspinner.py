from PIL import Image, ImageOps
from sys import argv

reverse = lambda a: [a[-1]] + reverse(a[:-1]) if len(a) > 0 else []

image = Image.open("centered-logo.png" if not len(argv) > 1 else argv[1]).resize((512, 512))
final = Image.new("RGBA", image.size, "WHITE")
final.paste(image, (0, 0), image)

final_inverted = ImageOps.invert(final.convert("RGB"))


frames = [final.rotate((i*24)/3) for i in range(15)]
reverse_frames = reverse(frames)
# shitty hack
fix = [Image.new("RGBA", frame.size, "WHITE") for frame in reverse_frames]
for fixed_frame, frame in zip(fix, reverse_frames):
    fixed_frame.paste(frame, (0, 0), frame)
# end shitty hack

inverted_frames = [final_inverted.rotate((i*24)/3) for i in range(15)]

reverse_inverted_frames = reverse(inverted_frames)

frames[0].save("fspinner.gif", save_all=True, append_images=frames[1:], optimize=True, loop=0, duration=60)
fix[0].save("fspinner-reverse.gif", save_all=True, append_images=fix[1:], optimize=True, loop=0, duration=60)
inverted_frames[0].save("inverted-fspinner.gif", save_all=True, append_images=inverted_frames[1:], optimize=True, loop=0, duration=60)
reverse_inverted_frames[0].save("inverted-reversed-fspinner.gif", save_all=True, append_images=reverse_inverted_frames[1:], optimize=True, loop=0, duration=60)

# create the speedyboi
speedyboi = [final.rotate(360-(i*24)) for i in range(int(15/3))]
speedyboi[0].save("speedyboi.gif", save_all=True, append_images=speedyboi[1:], loop=0, optimize=True, duration=25)