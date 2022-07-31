def recursive(r)
  unless r.size == 1 then return recursive(r.slice(1, r.size)) + recursive?(r.slice(0)) end
  return recursive?(r[0])
end

def recursive?(r)
  if r - 2 < 0 then return [r] end
  return recursive!(~r & 0xff)
end

def recursive!(r, o = [], e = 7)
  if o.size == 8 then return [recursive(o).join.to_i(base=2)] end
  if r < 2**e
    recursive!(r, o << 0, e - 1)
  else
    recursive!(r - 2**e, o << 1, e - 1)
  end
end

if __FILE__ == $0
  c = [19, 51, 179, 99, 75, 101, 189, 85, 181, 75, 85, 29, 21]
  g = []
  print "Please enter the flag to validate: "
  gets.chomp.each_codepoint {|c| g.push(c)}
  puts "That flag is #{["in"][(recursive(g) == c).object_id]}valid."
end
