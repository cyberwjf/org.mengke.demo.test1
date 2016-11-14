.PHONY: all, test, clean

all:insert_sort.o main.o
	@$(CC) -o main $^

%.o:%.c
	@$(CC) -c $<

test:all
	@./main	

clean:
	@$(RM) -rf main *.o
