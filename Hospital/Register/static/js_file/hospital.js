document.addEventListener("DOMContentLoaded", function() {
    const doctorSelect = document.getElementById("doctor");
    const dateInput = document.getElementById("date");
    const slotSelect = document.getElementById("slot");

    function fetchSlots() {
        const doctorId = doctorSelect.value;
        const date = dateInput.value;
        console.log("Doctor:", doctorId, "Date:", date);

        if (doctorId && date) {
            fetch(`/get-slots/?doctor_id=${doctorId}&date=${date}`)

                .then(response => response.json())
                .then(data => {
                    console.log("Slots data:", data);

                    // Clear old options
                    slotSelect.innerHTML = "";
                    const defaultOption = document.createElement("option");
                    defaultOption.textContent = "-- Select Slot --";
                    defaultOption.disabled = true;
                    defaultOption.selected = true;
                    slotSelect.appendChild(defaultOption);

                    let allSlots = [];

                    if (Array.isArray(data.slots)) {
                        allSlots.push(...data.slots.map(s => ({ ...s, booked: false })));
                        console.log(allSlots)
                    }
                    if (Array.isArray(data.book)) {
                        allSlots.push(...data.book.map(s => ({ ...s, booked: true })));
                    }

   
                    allSlots.sort((a, b) => {
                        return a.start.localeCompare(b.start);
                    });

                    // Append sorted slots
                    if (allSlots.length > 0) {
                        allSlots.forEach(slot => {
                            const option = document.createElement("option");
                            option.value = slot.start;
                            option.textContent = `${slot.start} - ${slot.end}`;
                            if (slot.booked) {
                                option.disabled = true; // booked slot
                                option.textContent += " (Booked)";
                            }
                            slotSelect.appendChild(option);
                        });
                    } else {
                        const option = document.createElement("option");
                        option.textContent = "No Available Slots";
                        option.disabled = true;
                        slotSelect.appendChild(option);
                    }
                })
                .catch(error => {
                    console.error("Error fetching slots:", error);
                });
        }
    }

    doctorSelect.addEventListener("change", fetchSlots);
    dateInput.addEventListener("change", fetchSlots);
});