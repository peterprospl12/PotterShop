{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License 3.0 (AFL-3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}
<section class="featured-products clearfix">
  <h2 class="h2 products-section-title text-uppercase">
    {l s='Polecane produkty' d='Shop.Theme.Catalog'}
  </h2>
  {include file="catalog/_partials/productlist.tpl" products=$products cssClass="row" productClass="col-xs-12 col-sm-6 col-lg-4 col-xl-3"}
  {if isset($total_pages) && $total_pages > 1}
    <div class="custom-pagination">
      {if $current_page > 1}
        <a href="?page={$current_page - 1}" class="btn btn-direction">
          <img src="https://localhost:18866/themes/child_classic/modules/ps_featuredproducts/img/custom-pagination-left.svg"
            alt="Shopping cart">
        </a>
      {/if}
      {if $current_page <= 1}
        <a href="?page=1" class="btn btn-direction">
          <img src="https://localhost:18866/themes/child_classic/modules/ps_featuredproducts/img/custom-pagination-left.svg"
            alt="Shopping cart">
        </a>
      {/if}
      {for $i = 1 to $total_pages}
        <a {if $i != $current_page}href="?page={$i}"{/if} class="btn {if $i == $current_page}btn-primary{else}btn-default{/if}">
          {$i}
        </a>
      {/for}

      {if $current_page < $total_pages}
        <a href="?page={$current_page + 1}" class="btn btn-direction">
          <img src="https://localhost:18866/themes/child_classic/modules/ps_featuredproducts/img/custom-pagination-right.svg"
            alt="Shopping cart">
        </a>
      {/if}
    </div>
  {/if}
</section>