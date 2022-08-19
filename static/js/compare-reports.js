const actualReport = document.getElementById('actual_report')
const previousReport = document.getElementById('previous_report')

const switcher = document.getElementById('switcher')

switcher.addEventListener('click', () => {
  actualReport.classList.toggle('hidden')
  previousReport.classList.toggle('hidden')

  return true;
})
