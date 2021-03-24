

public class CreditAccount extends BankAccount {

    private double creditLimit;
    private double loanRate;

    public CreditAccount(String accountNumber, String bankCode, double deposit, double creditLimit, double loanRate){

        super(accountNumber, bankCode, deposit);
        this.creditLimit = creditLimit;
        this.loanRate = loanRate;
    }

    public double getCreditLimit(){

        return this.creditLimit;
    }

    public double getLoanRate(){

        return this.loanRate;
    }

    public String toString(){

        return super.toString() + ", credit limit " + this.creditLimit + ", loan rate " + this.loanRate;
    }
}