rules = Array.from(document.getElementsByClassName('rule'))

rules.forEach(el => el.addEventListener('click', () => {
  const rule = el.dataset.rule
  const message = document.getElementById(`rule-message-${rule}`)

  message.classList.toggle('hidden')
}))

