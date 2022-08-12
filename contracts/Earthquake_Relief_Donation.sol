// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

contract Earthquake_Relief_Donation {

    //address of the owner (who deployed the contract)
    address public immutable owner;

    // min donation is 0.01 Eth
    uint256 public constant MIN_DONATION = 10000000000000000;

    //mapping to store which address donated how much ETH
    mapping(address => uint256) public s_addrToAmt;
    
    // array of addresses who donated
    address[] public s_doners;


    // the address that deploy the contract is the owner
    constructor()  {
        owner = msg.sender;
    }
    
    //addresses other than owner only can donate
    function donate() public payable onlyNotOwner{
        //is the donated amount less than MIN_DONATION?
        uint amount = msg.value;
        address doner = msg.sender;
        require(amount >= MIN_DONATION, "Min amount is 0.01Eth");

        // console.log("%s donated %s", doner, amount);  
        //if not, add to mapping 
        s_addrToAmt[doner] += amount;
        s_doners.push(doner);
    }
    
 
    //modifier: https://medium.com/coinmonks/solidity-tutorial-all-about-modifiers-a86cf81c14cb
    modifier onlyOwner {
        require(msg.sender == owner); 
        _;
    }

    modifier onlyNotOwner {
        require(msg.sender != owner);
        _;
    }

    // onlyOwner can withdraw the amount
    function collect_donated_amount() payable onlyOwner public {

        uint donated_amount = address(this).balance;
        require (donated_amount > 0 ,  "No deposit");

        // console.log("Total donation collection =  %s ", donated_amount);  
        payable(owner).transfer(donated_amount);
        
        address[] memory funders= s_doners;
        
        //deposited amount has been withdrawn, iterate through all the mappings and make them 0
        for (uint index=0; index < funders.length; index++){
            address funder = funders[index];
            s_addrToAmt[funder] = 0;
        }
        //s_doners array will be reset to 0
        s_doners = new address[](0);
    }
}

