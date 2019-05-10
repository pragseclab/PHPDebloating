<?php

/* privileges/resource_limit_item.twig */
class __TwigTemplate_82995701ca07cc21954a21a903dea0c93eb4c5ecd7c6612e0ee9f4d37c980ea2 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<div class=\"item\">
    <label for=\"text_";
        // line 2
        echo twig_escape_filter($this->env, $this->getAttribute((isset($context["limit"]) ? $context["limit"] : null), "input_name", array(), "array"), "html", null, true);
        echo "\">
        <code>
        <dfn title=\"";
        // line 4
        echo twig_escape_filter($this->env, $this->getAttribute((isset($context["limit"]) ? $context["limit"] : null), "description", array(), "array"), "html", null, true);
        echo "\">
            ";
        // line 5
        echo twig_escape_filter($this->env, $this->getAttribute((isset($context["limit"]) ? $context["limit"] : null), "name_main", array(), "array"), "html", null, true);
        echo "
        </dfn>
        </code>
    </label>
    <input type=\"number\" name=\"";
        // line 9
        echo twig_escape_filter($this->env, $this->getAttribute((isset($context["limit"]) ? $context["limit"] : null), "input_name", array(), "array"), "html", null, true);
        echo "\" id=\"text_";
        echo twig_escape_filter($this->env, $this->getAttribute((isset($context["limit"]) ? $context["limit"] : null), "input_name", array(), "array"), "html", null, true);
        echo "\"
        value=\"";
        // line 10
        echo twig_escape_filter($this->env, $this->getAttribute((isset($context["limit"]) ? $context["limit"] : null), "value", array(), "array"), "html", null, true);
        echo "\" title=\"";
        echo twig_escape_filter($this->env, $this->getAttribute((isset($context["limit"]) ? $context["limit"] : null), "description", array(), "array"), "html", null, true);
        echo "\" />
</div>
";
    }

    public function getTemplateName()
    {
        return "privileges/resource_limit_item.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  44 => 10,  38 => 9,  31 => 5,  27 => 4,  22 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "privileges/resource_limit_item.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/privileges/resource_limit_item.twig");
    }
}
