class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int g = 0;
        int i = 0;
        int j = 0;
         while(g < goal.length){
            if (i <cards1.length && cards1[i].equals(goal[g])){
                i++;
            }
            else if (j < cards2.length && cards2[j].equals(goal[g])){
                j++;
            }
            else {
                answer = "No";
                break;
            }
             g++;
        }
        return answer;
    }
}
