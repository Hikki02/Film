def simple_generator(val, count=0):
   while count < val:
       count += 1
       yield count

gen_iter = simple_generator(5)
print(next(gen_iter))
