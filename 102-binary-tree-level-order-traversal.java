class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        
        List<List<Integer>> res = new ArrayList<List<Integer>> ();
        
        LinkedList<TreeNode> curr = new LinkedList<TreeNode> ();
        LinkedList<TreeNode> next = new LinkedList<TreeNode> ();
        
        
        if (root == null) return res;
        curr.push(root);
        
        
        
        while (!curr.isEmpty()) {
            int len = curr.size();
            
            ArrayList<Integer> level = new ArrayList<Integer> ();

            for (int i=0; i<len; i++) {
                TreeNode node = curr.removeFirst();
                //System.out.println(node.val);
                

                level.add(node.val);
                
                if (node.left != null) next.add(node.left);
                if (node.right != null) next.add(node.right);
            }
            
            //System.out.println(level);
            res.add(level);
            
            curr = next;
        }

        
        
        return res;
    }
}
