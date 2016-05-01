
#!/usr/bin/python

import re
from argparse import ArgumentParser

arg_parser = ArgumentParser(description="Format an input file for TotD Workshop consumption")
arg_parser.add_argument(
    "-i",
    "--input-file",
    help="Input File",
    metavar="INPUT_FILE",
    dest="input_file",
    required=True
)
arg_parser.add_argument(
    "-m",
    "--min-characters",
    help="Minimum number of characters per line",
    metavar="MIN_CHARACTERS_PER_LINE",
    dest="min_characters",
    default=10
)
args = arg_parser.parse_args()

with open(args.input_file, "r") as input_file:
    input_data = input_file.read()

# All "removed" sequences are actually
# replaced with a space to preserve spacing.
# We then normalize the spacing with a final expression.

# Remove all non alphanumeric characters except for things that have special rules.
# This includes...
# Periods
# Question Marks
# Exclamation Points
# Single Quotes
# Hyphens 
formatted_data = re.sub("[^\w.?!'\-]", " ", input_data)

# Remove all underscores.
# Underscores are considered alphanumeric by Python...but I don't want em.
formatted_data = re.sub("_", " ", formatted_data)

# Remove any repeated hyphen sequences.
# This will keep hyphenated words like "low-budget".
formatted_data = re.sub("-{2,}", " ", formatted_data)

# Remove any single quotes that are preceded by spaces.
#
# This should leave contractions and most possessive words alone.
# Plural possessive nouns that end with "s" will get their
# single quote removed. :( 
formatted_data = re.sub("(?<=\s)'", " ", formatted_data)

# Remove any single quotes that are followed by spaces.
# See above regex for more information.
formatted_data = re.sub("'(?=\s)", " ", formatted_data)

# Remove any spacing between words and any following punctuation.
formatted_data = re.sub("\s+([.?!])", "\\1", formatted_data)

# Normalize all repeated whitespace down to a single space.
formatted_data = re.sub("\s{2,}", " ", formatted_data)

# Add a newline after question marks and exlamation points.
formatted_data = re.sub("([?!]+)", "\\1\n", formatted_data)

# Add a new line after periods when they are...
# * followed by whitespace.
# * NOT preceded by honorifics like (mrs. or mr.).
# ** Honorifics are matched when they are preceded by a space so a
#    sentence ending in "calms." doesn't trigger the "ms." honorific.
#
# Sentences that end with honorifics will not be matched correctly. :(
period_pattern = re.compile(
    "(?<!\smr)(?<!\smrs)(?<!\sms)(?<!\sdr)[.]\s+",
    re.IGNORECASE
)
formatted_data = period_pattern.sub(".\n", formatted_data)

min_characters = int(args.min_characters)
unique_lines = set()
for line in formatted_data.splitlines():
    stripped_line = line.strip()
    line_length = len(stripped_line)
    if line_length >= min_characters and line_length <= 50:
        unique_lines.add(stripped_line)

print "\n".join(unique_lines)