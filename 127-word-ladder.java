class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        
        Set<String> dict = new HashSet<String>(wordList);
        if (!dict.contains(endWord)) {
            return 0;
        }
        
        Queue<String> queue = new LinkedList<String>();
        Set<String> visited = new HashSet<String>();
        
        queue.add(beginWord);
        queue.add(null);
        
        int level = 1;
        
        while (!queue.isEmpty()) {
            String str = queue.poll();
            if (str != null) {
                for (int i=0; i<str.length(); i++) {
                    char[] chars = str.toCharArray();
                    for (char c='a'; c<='z'; c++) {
                        chars[i] = c;
                        
                        String newword = new String(chars);
                        
                        if (newword.equals(endWord) && dict.contains(newword)) return level+1;
                        
                        if (dict.contains(newword) && !visited.contains(newword)) {
                            queue.add(newword);
                            visited.add(newword);
                        }
                    }
                }
            }
            else {
                level++;
                if (!queue.isEmpty()) queue.add(null);
            
            }
        }
        
        return 0;
        
    }
}
