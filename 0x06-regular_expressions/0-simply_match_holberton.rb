#!/usr/bin/env ruby
# Creating script that accepts one arg and pass it to a regexp for matching
puts ARGV[0].scan(/Holberton/).join
