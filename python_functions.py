
# list of scores
scores_list = [ 67, 57, 89.5, 90.3, 95.2, 51.2, 43, 21, 17, 70, 77, 68, 69, 58, 61]
highest_score = max(scores_list)
lowest_score = min(scores_list)
average_score = sum(scores_list) / len(scores_list)

sorted_scores_list = sorted(scores_list)   # sort the scores
middle_index = len(scores_list) // 2      #  // means integer division, / means float division
median_score = sorted_scores_list[middle_index]

print(f"Number of scores: {len(scores_list)}")
print(f"Highest score: {highest_score}, Lowest score: {lowest_score}")
print(f"Average score: {average_score:.1f}")   # to 1 decimal point
print(f"Median score: {median_score}")