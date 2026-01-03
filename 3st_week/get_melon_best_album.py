def solution(genre_array, play_array):
	n = len(genre_array)
	genre_total_play_dict = {}
	genre_index_play_array_dict = {}
	result = []

	for i in range(n):
		genre = genre_array[i]
		play = play_array[i]
		if genre not in genre_total_play_dict:
			genre_total_play_dict[genre] = play
		else:
			genre_total_play_dict[genre] += play

	for i in range(n):
		genre = genre_array[i]
		play = play_array[i]
		if genre not in genre_index_play_array_dict:
			genre_index_play_array_dict[genre] = [[i, play]]
		else:
			genre_index_play_array_dict[genre].append([i, play])

	sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1],
	                                 reverse=True)

	for genre, total_play in sorted_genre_play_array:
		sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre],
		                                       key=lambda item: item[1], reverse=True)

		for song_index in sorted_genre_index_play_array[:2]:
			result.append(song_index)

	return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",
      solution(["classic", "pop", "classic", "classic", "pop"],
                           [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ",
      solution(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
                           [2000, 500, 600, 150, 800, 2500, 2000]))
