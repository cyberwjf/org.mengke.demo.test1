a = rand(100)

puts "Type a number from 0~99:"
b = gets

while a != b.to_i
    if a > b.to_i
        puts "Your number is smaller than the answer"
    else
        puts "Your number is bigger than the answer"
    end
    puts "Try again:"
    b=gets
end

puts "Biggo!"

