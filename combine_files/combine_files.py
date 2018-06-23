#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: Combine files

usage: combine_files.py [-h] [-o OUTDIR | -d] [-f FILEOUTNAME] dir type

Given files of a specified type, their text is combined into one file.

positional arguments:
  dir                   directory which contains files
  type                  type of file (eg: html, txt, md)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTDIR, --outdir OUTDIR
                        output file directory (default <dir>)
  -d, --default         use output directory specified in config.json
  -f FILEOUTNAME, --fileoutname FILEOUTNAME
                        output file name (default: `--combined.<type>`
"""
import argparse, os, sys

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from get_config import get_json_config

def create_dir(dir):
  # create dir if it doesn't exist
  if not os.path.exists(dir):
    os.makedirs(dir)

def combine_files(outfile_path, file_iterator, file_path):
  # Combines files with specified filetype
  with open(outfile_path, 'w') as outfile:
      for fname in file_iterator:
          fname = os.path.join(file_path, fname)
          with open(fname) as infile:
              for line in infile:
                  outfile.write(line)

  print('Success. see', outfile_path)

def get_args():
  parser = argparse.ArgumentParser(description="Given files of a specified type, their text is combined into one file.")
  group = parser.add_mutually_exclusive_group()
  group.add_argument("-o", "--outdir", help="output file directory (default <dir>)")
  group.add_argument("-d", "--default", action="store_true", help="use output directory specified in config.json")
  parser.add_argument("-f", "--fileoutname", help="output file name (default: `--combined.<type>`")
  parser.add_argument("dir", help="directory which contains files")
  parser.add_argument("type", help="type of file (eg: html, txt, md)")
  return parser.parse_args()

def create_file_iterator(file_path, file_type, outfile_name):
  filenames = os.listdir(file_path)
  return (x for x in filenames if x.endswith(file_type) and not x == outfile_name)

def main():
  args = get_args()
  filepath = args.dir

  if args.type.startswith('.'):
    filetype = args.type
  else:
    filetype = '.' + args.type

  if args.fileoutname:
    outfilename = args.fileoutname + filetype
  else:
    outfilename = '--combined' + filetype

  # handle output directory cases
  if args.default:
    # import the path from config
    config_dir = get_json_config()['directories']
    rootdir = config_dir['bookmarksRootDir']
    combined_dir = config_dir['combinedFiles']
    if combined_dir == '':
      outfilepath = os.path.join(rootdir, outfilename)
    else:
      create_dir(os.path.join(rootdir, combined_dir))
      outfilepath = os.path.join(rootdir, combined_dir, outfilename)
  elif args.outdir:
    create_dir(args.outdir)
    outfilepath = os.path.join(args.outdir, outfilename)
  else:
    outfilepath = os.path.join(filepath, outfilename)

  # print(filepath, filetype, outfilename, outfilepath, args.default, args.outdir)#debug

  file_generator = create_file_iterator(filepath, filetype, outfilename)

  combine_files(outfilepath, file_generator, filepath)

if __name__ == '__main__':
  main()