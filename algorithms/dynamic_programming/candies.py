n = int(input().strip())
ratings = [int(input().strip())]
candies = [1]

for i in range(1, n):
    ratings.append(int(input().strip()))
    reward = 1

    if ratings[i] > ratings[i-1]:
        reward = candies[i-1] + 1
    elif ratings[i] < ratings[i-1] and candies[i-1] <= reward:
        candies[i-1] =  2

    candies.append(reward)

total = candies[n-1]
for i in range(n-2, -1, -1):
    if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
        candies[i] = candies[i+1] + 1

    total += candies[i]

print(total)