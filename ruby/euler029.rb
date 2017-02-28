#!/usr/bin/ruby
puts (2..100).inject([]){|terms, a| (2..100).inject([]){ |placeholder, b| terms << (a**b)}}.uniq.length