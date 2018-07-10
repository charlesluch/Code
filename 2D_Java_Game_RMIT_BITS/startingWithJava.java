import java.io.*; // Error: no .* at the end, without it, err message: only type can be imported.

public class AccountManager {
	/* "Write a program to manage withdrawals from a bank account. If there are enough funds, the program should withdraw; otherwise it should reject." */
	// What is the initial value of the balance?
	// What kind of outputs should the program produce?
	/* "Write a program to manage withdrawals from a bank account. The program should accept the initial balance, and then accept a withdrawal. If there are enough funds, the program should accept the withdrawal, otherwise it should reject it. The program should display the new balance at the end of the transaction. Input comes from the keyboard and output goes to the screen." */

	// My writing of spec:

	// 1. prompt user for withdrawal amount
	// 2. check if amount requested exceeds amount in bank
//	    a. if so, process.
//	    b. if not, reject.

	// The way it was written in the notes:

	// 1. get balance
	// 2. get withdrawal
	// 3. decide accept or refuse

	// Psuedocode design from notes:

	// 1. get balance
//	        a. display prompt
//	        b. get balance value
	// 2. get withdrawal
//	        a. display prompt
//	        b. get balance value
	// 3. decide accept or refuse
//	        a. if balance greater than or equal to withdrawal, accept
//	            i. display accept message
//	           ii. calculate new balance
//	          iii. display new balance message and value
//	        b. otherwise reject
//	            i. display reject message
//	           ii. calculate new balance
//	          iii. display new balance message and value

	// Program with comments (written CL 29/6/18):

	// Error: public static void main(String[] args) { goes in class and after inport


	//	class ProcessWithdrawal  CamelCase all caps (err)
	   public static void main (String[] args) throws IOException
	   {
	// 1. get balance
//	        a. display prompt
//	        b. get balance value

//	    system.out.print("Enter initial balance: ");
//	    readline() WHAT I WROTE

	// Notes example:
	      BufferedReader stdin = new BufferedReader (new InputStreamReader(System.in)); // we need first to accept user input, also System is capitalized
	      String initString, withdrawString;
	      int initialBalance, withdrawal;    // we also need to declare variables

	// Me again:
	      System.out.print ("Enter initial balance: ");  // Error: not println, spaces for readability, removed ...ln to make the console output better aligned.
	      initString = stdin.readLine(); // Error: did not include assignment to variable, also, Line in readLine is capitalized
	      initialBalance = Integer.parseInt (initString); // Error: we have a string, but we haven't converted the type

	// 2. get withdrawal
//	        a. display prompt
//	        b. get balance value
	      System.out.print ("Enter withdrawal: ");
	      withdrawString = stdin.readLine(); // Error: typo on variable name
	      withdrawal = Integer.parseInt (withdrawString); // Error: we have a string, but we haven't converted the type

	// 3. decide accept or refuse
//	        a. if balance greater than or equal to withdrawal, accept
//	            i. display accept message
//	           ii. calculate new balance
//	          iii. display new balance message and value

	      if (withdrawal <= initialBalance)
	      {
	         System.out.println ("Withdrawal accepted.");
//	       int balance = initialBalance - withdrawal; // Error: cannot combine vars of differing types, Efficiency: better way shown
	         System.out.print ("New Balance: ");
	         System.out.println (initialBalance - withdrawal);
	      }

//	        b. otherwise reject
//	            i. display reject message
//	           ii. calculate new balance
//	          iii. display new balance message and value

	      else
	      {
	         System.out.println ("Withdrawal rejected.");
//	       int balance = initialBalance;
//	       System.out.println ("New balance: ", balance);
	         System.out.print ("New Balance: ");
	         System.out.println (initialBalance);
	      }
	   }
	}
