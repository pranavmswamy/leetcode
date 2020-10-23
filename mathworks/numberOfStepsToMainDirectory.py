For question 1: Number of steps to Main Directory
Algorithm : 

1. Use stack to store paths. 
2. Whenever there is a "./" value in list ignore that value.
3. When there is "../" value in list if stack is not empty then pop the topmost value.
4. Else keeping on adding directories.
5. stack size is the answer in end.

public static int minimumSteps(List loggedMoves) {
Stack stack = new Stack<>();
for(String s:loggedMoves) {
if(s.equals("./")) {
continue;
}
else if(s.equals("../")) {
if(!stack.isEmpty()) {
stack.pop();
}
}
else {
stack.push(s);
}
}

	return stack.size();
}
