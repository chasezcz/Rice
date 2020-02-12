import request from '@/utils/request'

export function getDeliveryInfo() {
  return request({
    url: '/warehouse/getDeliveryInfo',
    method: 'get'
  })
}

export function delivery(data) {
  return request({
    url: '/warehouse/delivery',
    method: 'get',
    params: { data }
  })
}

export function collect(data) {
  return request({
    url: '/warehouse/collect',
    method: 'get',
    params: { data }
  })
}

export function statisticsToday() {
  return request({
    url: '/warehouse/statisticsToday',
    method: 'GET'
  })
}
