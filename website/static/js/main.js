document.addEventListener('DOMContentLoaded', function () {

    function getAll(selector) {
        return Array.prototype.slice.call(document.querySelectorAll(selector), 0);
    }


    let $modals = getAll('.modal');
    let $galleryButtons = getAll('.gallery-button');
    let $modalButtons = getAll('.modal-button');
    let $modalCloses = getAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button');

    if ($modalButtons.length > 0) {
        $modalButtons.forEach(function ($el) {
            $el.addEventListener('click', function () {
                let target = $el.dataset.target;
                let src_url = $el.dataset.url;
                let order = $el.dataset.order;
                openModal(target, src_url, order);
            });
        });
    }

    if ($modalCloses.length > 0) {
        $modalCloses.forEach(function ($el) {
            $el.addEventListener('click', function () {
                closeModals();
            });
        });
    }

    if ($galleryButtons.length > 0) {
        $galleryButtons.forEach(function ($el) {
            $el.addEventListener('click', function () {
                if ($el.dataset.url) {
                    let target = $el.dataset.target;
                    let src_url = $el.dataset.url;
                    let order = $el.dataset.order;
                    openModal(target, src_url, order);
                }
            });
        });
    }

    function openModal(target, src_url, order) {
        let $target = document.getElementById(target);
        let $target_image = document.getElementById('modal-img');
        $target_image.src = src_url;
        $target.classList.add('is-active');

        if (typeof order !== 'undefined') {
            if ($galleryButtons.length > 0) {
                $galleryButtons.forEach(function ($el) {
                    $el.classList.add('is-active');

                    let next_image = parseInt(order, 10);
                    next_image = ($el.id === "gallery-previous") ? next_image - 1 : next_image + 1;

                    let target_image = document.getElementById("gallery-image-" + next_image)

                    if (target_image) {
                        $el.disabled = false;
                        $el.dataset.url = target_image.dataset.url;
                        $el.dataset.order = target_image.dataset.order;
                    } else {
                        $el.disabled = true;
                        $el.removeAttribute("data-url")
                    }
                });
            }
        }
    }

    function closeModals() {
        $modals.forEach(function ($el) {
            $el.classList.remove('is-active');
        });
        $galleryButtons.forEach(function ($el) {
            $el.classList.remove('is-active');
        });
    }
});
