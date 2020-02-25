#!/usr/bin/env ruby
#Creating Ruby script that finds [SENDER],[RECEIVER],[FLAGS] from a command line argument
puts ARGV[0].scan(/\[from(.*?)\]|\[to(.*?)\]|\[flags(.*?)\]/).join
