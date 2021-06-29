
    
class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        int number = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if (i < s.length() - 1) {
                if (map.get(ch) < map.get(s.charAt(i + 1))) {
                    number -= map.get(ch);
                    continue;
                }
            }
            number += map.get(ch);
        }
        return number;
    }
}


'if you see ArrayList<Integer> for example, that means "An ArrayList of Integers." Many classes use generics to constrain the type of the elements in a container, for example. Another example is HashMap<String, Integer>, which means "a map with String keys and Integer values."'