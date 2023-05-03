#!/usr/bin/env ruby
sender = ARGV[0].scan(/(?<=from:)\+?\w*[^\]]/).join
receiver = ARGV[0].scan(/(?<=to:)\+?\w*[^\]]/).join
flag = ARGV[0].scan(/(?<=flags:)-?[01]:-?[01]:-?[01]:-?[01]:-?[01]/).join
output = sender + "," + receiver + "," + flag
puts output
