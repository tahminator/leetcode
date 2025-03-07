package com.tahminator.leetcode.l355_design_twitter;

/**
 * We can keep a track of a list of userIds that map
 * to a list of their posts.
 * As for following, we can just use an array of hashsets to check who is folowing who.
 */
class Twitter {
    // We are going to be using the value to store what Epoch timestamp it was created.
    private int count;
    private final List<Map.Entry<Integer, Integer>>[] posts;
    private final Set<Integer>[] following;

    public Twitter() {
      count = 0;
      posts = new List[500];
      following = new Set[500];

      for (int i = 0; i < 500; i++) {
        posts[i] = new ArrayList<>();
      }

      for (int i = 0; i < 500; i++) {
        following[i] = new HashSet<>();
      }
    }
    
    public void postTweet(int userId, int tweetId) {
      posts[userId].add(Map.entry(tweetId, ++count));
    }
    
    public List<Integer> getNewsFeed(int userId) {
      Queue<Map.Entry<Integer, Integer>> q = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
      
      Set<Integer> fSet = following[userId];
      for (Integer fId : fSet) {
        List<Map.Entry<Integer, Integer>> fp = posts[fId];
        for (Map.Entry<Integer, Integer> p : fp) {
          q.offer(p);
        }
      }
      
      List<Map.Entry<Integer, Integer>> mp = posts[userId];
      for (Map.Entry<Integer, Integer> p : mp) {
        q.offer(p);
      }
        
      List<Integer> res = new ArrayList<>();
      
      int i = 0;

      while (!q.isEmpty() && i < 10) {
        Map.Entry<Integer, Integer> pair = q.poll();
        res.add(pair.getKey());
        i++;
      }

      return res;
    }
    
    public void follow(int followerId, int followeeId) {
      following[followerId].add(followeeId);
      
    }
    
    public void unfollow(int followerId, int followeeId) {
      following[followerId].remove(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
