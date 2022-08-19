// Handle the `page_url` input errors

const page_url_input = document.getElementById('page_url')
const error_msg = document.getElementById('page_url_error')

if (page_url_input && error_msg) {
  page_url_input.addEventListener('keydown', e => {
    if (error_msg) {
      e.target.classList.replace('border-red-600', 'border-black')
      error_msg.remove()
    }
  }, {once: true})
}



