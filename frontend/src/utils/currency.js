const currency = (amount) => {
    return "৳" + parseFloat(amount).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
}

export default currency;