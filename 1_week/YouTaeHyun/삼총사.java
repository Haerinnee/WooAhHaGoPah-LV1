class Solution {
    public int solution(int[] number) {
        int answer = 0;
		int count = 0;
		int sum = 1;
		for(int i = 0; i < number.length - 2; i++) {
			for(int j = i + 1; j < number.length; j++) {
				for(int k = j + 1; k < number.length; k++) {
					sum = number[i] + number[j] + number[k];
					if(sum == 0) {
						count++;
						sum = 1;
					}
				}
			}
		}
        answer = count;
        return answer;
    }
}
