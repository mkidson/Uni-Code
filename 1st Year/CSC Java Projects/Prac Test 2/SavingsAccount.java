


public class SavingsAccount extends BankAccount {

    private double interestRate;

    public SavingsAccount(String accountNumber, String bankCode, double deposit, double interestRate){

        super(accountNumber, bankCode, deposit);
        this.interestRate = interestRate;
    }

    public double getInterestRate(){

        return this.interestRate;
    }

    public String toString(){

        return super.toString() + ", interest rate " + this.interestRate;
    }
}