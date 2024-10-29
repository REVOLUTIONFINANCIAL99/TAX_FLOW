const Web3 = require('web3');
const web3 = new Web3('http://localhost:8545'); // Cambia a tu endpoint de RPC

const contractABI = [ /* ABI del contrato aquí */ ];
const contractAddress = '0x...'; // Dirección del contrato desplegado

const myContract = new web3.eth.Contract(contractABI, contractAddress);

// Ejemplo para establecer un valor
async function setStoredData(value) {
    const accounts = await web3.eth.getAccounts();
    await myContract.methods.set(value).send({ from: accounts[0] });
}

// Ejemplo para obtener un valor
async function getStoredData() {
    const result = await myContract.methods.get().call();
    console.log(result);
}
