import colorgram

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
    hex_colors.append(rgb_to_hex((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)))

  html="""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
  body { margin: 0; }
  grid.xxxx {
    display: inline-grid;
    grid-template-columns: min-content min-content min-content min-content;
  }
  box {
    width: 250px;
    height: 250px;
  }
  </style>
</head>
<body>
  <grid class="xxxx">"""
  for color in repeat(hex_colors, 16):
    html+='\n    <box style="background: #' + color + ';"></box>'
  html+="""
  </grid>
</body>
</html>"""
  f = open("../../build/html/{}.html".format(pokemon_id), "w")
  f.write("".join(html))
  f.close()
