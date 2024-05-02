
class two_sum:
    def main(self):
        nums = [1,2,3,4]
        target = 5
        counter = 0
        for i in range(len(nums)):
                val = nums[i]
                if val == nums[i]:
                    var = nums[counter] + nums[-1]
                    if var == target:
                        print(var)
                        break
                    else:
                        counter +=1
                
if __name__ == "__main__":     
    instance = two_sum()
    instance.main()

# add 2 numbers by index
# indexing [i]
# now we are going through the entire list.