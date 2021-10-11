# these are the only two different spaces of uniform size that Twitter allows (space and nb-space)
# other similar characters (e.g. "punctuation space") get mapped back to a normal space
# they hence do not guarantee non-identity of tweets, since Twitter views them as the same
space_characters = {
  "Space": "\u0020",
  "No-Break Space": "\u00A0",
}

# use this to add non-identity by inserting a random number after the others
zero_width_space = "\u200B"