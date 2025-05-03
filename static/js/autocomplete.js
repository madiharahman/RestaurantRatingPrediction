function autocompleteRestaurantName() {
  const input = document.getElementById("name");
  const list = document.getElementById("suggestions");

  input.addEventListener("input", function () {
    const query = this.value.trim();  // Get the value and trim any extra spaces
    if (query.length < 2) {
      list.innerHTML = "";  // Don't show anything if the query is too short
      return;
    }

    fetch(`/suggest?q=${query}`)
      .then(response => response.json())
      .then(data => {
        list.innerHTML = "";  // Clear previous suggestions

        if (data.length > 0) {
          data.forEach(item => {
            const option = document.createElement("div");
            option.textContent = item;
            option.className = "suggestion-item";
            option.onclick = () => {
              input.value = item;  // Set the input value to the clicked suggestion
              list.innerHTML = "";  // Clear the suggestions
            };
            list.appendChild(option);
          });
        } else {
          const noResult = document.createElement("div");
          noResult.textContent = "No matches found.";
          noResult.className = "suggestion-item";
          list.appendChild(noResult);
        }
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        list.innerHTML = "";  // Clear suggestions on error
      });
  });

  // Hide suggestion box if clicked outside
  document.addEventListener("click", function (e) {
    if (!input.contains(e.target) && !list.contains(e.target)) {
      list.innerHTML = "";  // Clear suggestions when clicking outside
    }
  });
}

window.onload = autocompleteRestaurantName;
