<template>
  <div>
    <el-form class="collectForm">

      <!-- 选择货品 -->
      <el-form-item>
        <div>
          <span style="font-size:35px">增进货品：</span>
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
            <el-table-column label="新进量">
              <template slot-scope="{row}">
                <el-input v-model="row.collectNum">{{ row.collectNum }}</el-input>
              </template>
            </el-table-column>
          </el-table>

        </div>
      </el-form-item>
      <el-form-item>
        <el-button class="btn" type="primary" @click="collectSubmit(productAll)">确定进货</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { getDeliveryInfo, collect } from '@/api/warehouse'
export default {
  data() {
    return {
      productAll: this.productAll,
      products: []
    }
  },
  created: function() {
    getDeliveryInfo().then(response => {
      this.productAll = response.data['products']
    }).catch(_ => {
      this.productAll = []
    })
  },
  methods: {
    collectSubmit(pa) {
      pa.forEach(product => {
        if (product.deliveryNum !== undefined) {
          this.products.push({
            'label': product.label,
            'number': product.deliveryNum
          })
        }
      })
      collect(this.products)
      this.$message({
        message: '进货成功！',
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
