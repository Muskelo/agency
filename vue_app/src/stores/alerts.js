import {defineStore} from 'pinia'


export const useAlertsStore = defineStore('alerts', {
    state: () => {
        return {
            data: Array()
        }
    },
    actions: {
        async addAlert(title, message, type = "info") {
            let alert_ = {title: title, message: message, type: type, time: Date.now()}
            this.data.push(alert_);

            // delete after delay
            setTimeout(() => {
                let index = this.data.indexOf(alert_);
                this.deleteAlert(index)
            }, 10000)
        },
        deleteAlert(index) {
            this.data.splice(index, 1);
        },
    }
})
