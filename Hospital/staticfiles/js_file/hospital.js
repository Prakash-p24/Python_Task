document.addEventListener("DOMContentLoaded", function() {
    const doctorSelect = document.getElementById("doctor");
    const dateInput = document.getElementById("date");
    const slotSelect = document.getElementById("slot");

    function fetchSlots() {
        const doctorId = doctorSelect.value;
        const date = dateInput.value;
        console.log("Doctor:", doctorId, "Date:", date); 

        if (doctorId && date) {
            fetch("{% url 'get_slots' %}?doctor_id=" + doctorId + "&date=" + date)
                .then(response => response.json())
                .then(data => {
                    console.log("Slots data:", data); 
                    slotSelect.innerHTML = '<option value="">-- Select Slot --</option>';
                        if (data.slots.length > 0) {
                           data.slots.forEach(slot => {
                           const option = document.createElement("option");
                           option.value = slot.start;
                            option.textContent = `${slot.start} - ${slot.end}`;
                            slotSelect.appendChild(option);
                          });
}                       else {
                            const option = document.createElement("option");
                            option.textContent = 'No Available Slots';
                            slotSelect.appendChild(option);
}

                        if (data.book && data.book.length > 0) {
                             data.book.forEach(books => {
                             const option = document.createElement("option");
                             option.value = books.start;
                             option.textContent = `${books.start} - ${books.end}`;
                             option.disabled = true; 
                            slotSelect.appendChild(option);
    });
}                       
                })
                .catch(err => console.error("Error fetching slots:", err));
        }
    }

    doctorSelect.addEventListener("change", fetchSlots);
    dateInput.addEventListener("change", fetchSlots);
});
