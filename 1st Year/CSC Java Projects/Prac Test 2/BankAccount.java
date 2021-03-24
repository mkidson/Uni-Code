


public class BankAccount {

    private String accountNumber;
    private String bankCode;
    private double deposit;

    public BankAccount(String accountNumber, String bankCode, double deposit) {

        this.accountNumber = accountNumber;
        this.bankCode = bankCode;
        this.deposit = deposit;
    }

    public String getAccountNumber(){

        return this.accountNumber;
    }

    public String getBankCode(){

        return this.bankCode;
    }

    public double getDeposit(){

        return this.deposit;
    }

    public boolean equals(BankAccount other){

        boolean isEqual = false;
        if (this.accountNumber.equals(other.getAccountNumber()) && this.bankCode.equals(other.getBankCode())) {
            
            isEqual = true;
        }

        return isEqual;
    }

    public String toString(){

        return "Account number " + this.accountNumber + ", bank code " + this.bankCode + ", balance R" + this.deposit;
    }
}