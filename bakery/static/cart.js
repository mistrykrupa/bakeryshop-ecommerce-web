function increaseQuantity(button) {
    const input = button.parentElement.querySelector('input');
    input.value = parseInt(input.value) + 1;
  }

  function decreaseQuantity(button) {
    const input = button.parentElement.querySelector('input');
    if (parseInt(input.value) > 1) {
      input.value = parseInt(input.value) - 1;
    }
  }

  function removeItem(button) {
    const row = button.parentElement.parentElement;
    row.remove();
    updateTotal();
  }

  function editItem(button) {
    // Add functionality for editing item details
    alert('Editing item functionality');
  }

  function updateCart() {
    // Add functionality to update cart, if needed
    alert('Updating cart functionality');
    updateTotal();
  }

  function updateTotal() {
    // Add functionality to update total price
    const totalElement = document.querySelector('.total-price');
    // Calculate and set the total price based on the product prices and quantities
  }