import colorgram
import subprocess

# convert rgb to hex
def rgb_to_hex(rgb): return '%02x%02x%02x' % rgb

# repeat array until length is met
def repeat(seq, length):
  multiple, remainder = divmod(length, len(seq))
  return seq * multiple + seq[:remainder]

# for each pokemon
for pokemon_id in range(1, 252):
  print("#", pokemon_id, sep="")

  # extract an rgb palette from the png
  colors = colorgram.extract("../assets/pokemon/{:03}_00.png".format(pokemon_id), 16)
  # define array
  hex_colors = []
  # convert the colors to hex and put them in the array
  for i in range(len(colors)):
    hex_colors.append("#" + rgb_to_hex((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)))

  f = open("../../build/txt/{}.txt".format(pokemon_id), "w")
  f.write(" ".join(repeat(hex_colors, 16)))
  f.close()

subprocess.call("./rename.sh", shell=True)
