import argparse

def get_args(desc_str, infile_obj, outfile_obj):
  '''obj: {
    flag: ''
    help: ''
  }
  '''
  parser = argparse.ArgumentParser(description=desc_str)
  inflag = infile_obj['flag']
  outflag = outfile_obj['flag']
  parser.add_argument(inflag, help=infile_obj['help'])
  parser.add_argument(outflag, help=outfile_obj['help'])
  return parser.parse_args()
