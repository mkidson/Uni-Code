import java.util.Scanner;

/**
 * CSC1016S Practest2E code given to students
 *
 * @version 1.0
 */
public class TestE {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int option;
        BankAccount[] bankAccounts = new BankAccount[100];
        int index = 0;
        System.out.println("**** Welcome to the CS banking system ****");

        do {
            System.out.println("Enter choice: ");
            System.out.println("1. Add new bank account (not savings or credit account).");
            System.out.println("2. Add savings bank account.");
            System.out.println("3. Add credit bank account.");
            System.out.println("4. Quit");
            option = s.nextInt();
            s.nextLine();
            if (option != 4) {
                System.out.println("Enter bank code:");
                String bankCode = s.nextLine();
                System.out.println("Enter account number:");
                String accountNumber = s.nextLine();
                System.out.println("Enter initial deposit (in Rands):");
                double deposit=s.nextDouble();
                s.nextLine();

                BankAccount newBankAccount = null;
                switch (option) {
                    case 1:
                        newBankAccount = new BankAccount(accountNumber, bankCode, deposit);
                        break;
                    case 2:
                        System.out.println("Enter the interest rate:");                  
                        newBankAccount = new SavingsAccount(accountNumber, bankCode, deposit, s.nextDouble());
                        s.nextLine();
                        break;
                    case 3:
                        System.out.println("Enter the credit limit (in Rands):");
                        double creditLimit=s.nextDouble();
                        s.nextLine();
                        System.out.println("Enter the loan rate:");
                        newBankAccount = new CreditAccount(accountNumber, bankCode, deposit, creditLimit, s.nextDouble());
                }

                
                boolean duplicate = false;
                for (int i = 0; i < bankAccounts.length; i++) {
                    BankAccount bankAccount = bankAccounts[i];
                    if (bankAccount != null && bankAccount.equals(newBankAccount)) {
                        System.out.println("A bank account with that number and branch code already exists: \n" + bankAccount);
                        duplicate = true;
                    }
                }
                if (!duplicate) {
                    bankAccounts[index++] = newBankAccount;
                }
            }
        } while (option != 4);
        System.out.println("Showing all bank accounts in the inventory:");
        for (int i = 0; i < bankAccounts.length; i++) {
            BankAccount bankAccount = bankAccounts[i];
            if (bankAccount != null) {
                System.out.println(bankAccount);
            }
        }
    }

}
