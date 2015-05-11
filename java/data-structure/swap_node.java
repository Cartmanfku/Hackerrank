import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class swap_node {
	
	private static Node[] nodes;
	private static int max_depth;
	
	private static class Node {
		private int parent =0;
		private int left = 0;
		private int right = 0;
		
		private int depth = 0;
		private int value = 0;
	}
	
	private static void InOrderPrint(int x) {
		Node n = nodes[x];
		if (n.left != -1) {
			InOrderPrint(n.left);
		}
		System.out.print(n.value + " ");
		if (n.right != -1) {
			InOrderPrint(n.right);
		}
	}
	
	private static void swap(int k, int N) {
		int nextK = k;
		while (nextK + 1 <= max_depth) {
			for (int i=1;i<N+1;i++) {
				if (nodes[i].depth == nextK) {
					int tmp = nodes[i].left;
					nodes[i].left = nodes[i].right;
					nodes[i].right = tmp;
				}
			}
			nextK = nextK + k ;
		}
	}


    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int N;
        int a,b;
        N = in.nextInt();
        nodes = new Node[N+1]; 
        for (int i=1;i<N+1;i++) {
        	nodes[i] = new Node();
        }
        
        for (int i=1;i<N+1;i++) {
            a = in.nextInt();
            b = in.nextInt();
            nodes[i].value = i;
            nodes[i].left = a;
            nodes[i].right = b;
            if (nodes[i].parent != 0) {
            	nodes[i].depth = nodes[nodes[i].parent].depth + 1;
            } else {
            	nodes[i].depth = 1;
            }
            if (nodes[i].depth > max_depth) {
            	max_depth = nodes[i].depth;
            }
            if (a != -1)
            	nodes[a].parent = i;
            if (b != -1)
            	nodes[b].parent = i;
            		
        }
        
        int T = in.nextInt();
        for (int i=0;i<T;i++) {
        	int s = in.nextInt();
        	swap(s,N);
        	InOrderPrint(1);
        	System.out.println();
        }
        
        
    
    }
}