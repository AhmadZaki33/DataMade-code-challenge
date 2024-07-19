/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

document
  .getElementById('address-form')
  .addEventListener('submit', function (event) {
    event.preventDefault()
    const address = document.getElementById('address').value
    fetch(`/api/parse/?address=${encodeURIComponent(address)}`)
      .then(response => response.json())
      .then(data => {
        const resultsDiv = document.getElementById('address-results')
        const parseType = document.getElementById('parse-type')
        const addressComponentsTable =
					document.getElementById('address-components')
        parseType.innerText = data.address_type
        addressComponentsTable.innerHTML = ''
        for (const [part, tag] of Object.entries(data.address_components)) {
          const row = document.createElement('tr')
          const partCell = document.createElement('td')
          const tagCell = document.createElement('td')
          partCell.innerText = part
          tagCell.innerText = tag
          row.appendChild(partCell)
          row.appendChild(tagCell)
          addressComponentsTable.appendChild(row)
        }
        resultsDiv.style.display = 'block'
      })
      .catch(error => {
        console.error('Error:', error)
      })
  })
