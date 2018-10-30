import sys
from copy import deepcopy
from PIL import Image

images = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png']

j = 0

def permute(a, l, r):
	global j
#	j += 1
	if l==r:
		all_images = []
		all_images.extend(a)

		images = map(Image.open, all_images)
		widths, heights = zip(*(i.size for i in images))
	
		total_width = sum(widths)
		max_height = max(heights)
		
		new_im = Image.new('RGB', (total_width, max_height))
		
		x_offset = 0
		for im in images:
			new_im.paste(im, (x_offset,0))
			x_offset += im.size[0]
		out = "out/" + str(j) + ".out.jpg"
		new_im.save(out)
		j += 1
		
	else:
		for i in xrange(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack

print("Make a directory called out")
pause()
permute(images, 0, len(images)-1)


print("ffmpeg -r 1/5 -i %d.out.jpg -c:v libx264 -vf fps=30 -pix_fmt yuv420p out.mp4")
