const dropdownBtn = document.getElementById('auth-menu-button')
const dropdownMenu = document.getElementById('auth-dropdown-menu')

dropdownBtn.addEventListener('click', () => {
  const hidden = dropdownMenu.classList.toggle('hidden')
  dropdownBtn.ariaExpanded = (! hidden).toString()
})
