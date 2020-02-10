<template>
  <div>
    <el-form class="deliverForm">
      <!-- 选择配送员 -->
      <el-form-item>
        <span style="font-size:35px">配送员：</span>
        <el-select v-model="salers" class="newSelect" multiple filterable allow-create default-first-option placeholder="请选择配送员或自定义">
          <!-- eslint-disable-next-line -->
          <el-option style="font-size:35px" v-for="saler in salerAll" :key="saler.value" :label="saler.label" :value="saler.value"></el-option>
        </el-select>

      </el-form-item>

      <!-- 选择货品 -->
      <el-form-item>
        <div>
          <span style="font-size:35px">配送货品：</span>
          <el-table border fit highlight-current-row :data="productAll" style="font-size:20px">
            <el-table-column label="货品" prop="label">
              <template slot-scope="{row}">
                <span>{{ row.label }}</span>
              </template>
            </el-table-column>
            <el-table-column label="库存量" prop="number">
              <template slot-scope="{row}">
                <span>{{ row.number }}</span>
              </template>
            </el-table-column>
            <el-table-column label="发出量">
              <template slot-scope="{row}">
                <el-input v-model="row.deliveryNum">{{ row.deliveryNum }}</el-input>
              </template>
            </el-table-column>
          </el-table>

        </div>
      </el-form-item>
      <el-form-item>
        <span style="font-size:35px">备注</span>
        <el-input v-model="remarks">{{ remarks }}</el-input>
      </el-form-item>
      <el-form-item>
        <el-button class="btn" type="primary" @click="deliverySubmit(productAll)">确定发货</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { getDeliveryInfo, delivery } from '@/api/warehouse'
export default {
  data() {
    return {
      salerAll: this.salerAll,
      productAll: this.productAll,
      salers: [],
      products: [],
      remarks: ''
    }
  },
  created: function() {
    getDeliveryInfo().then(response => {
      this.salerAll = response.data['salers']
      this.productAll = response.data['products']
    }).catch(_ => {
      this.salerAll = []
      this.productAll = []
    })
  },
  methods: {
    deliverySubmit(pa) {
      pa.forEach(product => {
        if (product.deliveryNum !== undefined) {
          this.products.push({
            'label': product.label,
            'number': product.deliveryNum
          })
        }
      })

      var data = {
        'products': this.products,
        'remarks': this.remarks,
        'time': new Date().toDateString()
      }
      delivery(data)
      this.$message({
        message: '发货成功！',
        type: 'success'
      })
      this.$router.push({ path: '/warehouse', query: this.otherQuery })
    }
  }
}
</script>

<style lang="scss" scoped>
.deliverForm {
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  position: relative;
  max-width: 100%;
  padding: 10px 40px 10px 40px;
  margin: 0 auto;
  overflow: hidden;
}
.btn {
  margin: 0, auto;
  padding: 20 80px 20px 80px;
  height: auto;
  width: 100%;
  font-size: 35px;
  position: relative;
}

</style>
